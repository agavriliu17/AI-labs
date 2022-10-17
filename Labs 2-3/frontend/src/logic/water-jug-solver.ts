import { NO_SOLUTION, STATE } from "./constants";
import { dangerousDeepClone } from "./utils";
import { Jug, JugState, HeuristicResult } from "./interfaces";

export class WaterJugSolver {
  queue: JugState[] = [];
  tree = new Map();
  pathList: JugState[][] = [];

  constructor(
    readonly xGallon: number,
    readonly yGallon: number,
    readonly zGallon: number
  ) {
    const [small, large] = [this.xGallon, this.yGallon].sort((a, b) => a - b);
    const start: JugState = {
      action: STATE.INITIAL,
      simple: "0,0",
      jugs: [
        { value: 0, capacity: small, name: "small" },
        { value: 0, capacity: large, name: "large" },
      ],
    };
    this.queue.push(start);
    this.addNode(this.getUniqueStringOutOfState(start));
    this.pathList.push([start]);
  }

  addNode(value: string) {
    if (!this.tree.has(value)) {
      this.tree.set(value, []);
    }
  }

  addEdge(left: string, right: string) {
    this.addNode(left);
    this.addNode(right);
    this.tree.get(left).push(right);
  }

  emptyJug(state: JugState, target: Jug["name"]): JugState {
    const newState = dangerousDeepClone(state);
    newState.action =
      target === "small" ? STATE.EMPTY_SMALL : STATE.EMPTY_LARGE;
    newState.jugs = newState.jugs.map((jug: Jug) => {
      if (jug.name === target) {
        jug.value = 0;
      }
      return jug;
    }) as JugState["jugs"];

    newState.simple = this.getUniqueStringOutOfState(newState);
    return newState;
  }

  fillJug(state: JugState, target: Jug["name"]): JugState {
    const newState = dangerousDeepClone(state);
    newState.action = target === "small" ? STATE.FILL_SMALL : STATE.FILL_LARGE;
    newState.jugs = newState.jugs.map((jug: Jug) => {
      if (jug.name === target) {
        jug.value = jug.capacity;
      }
      return jug;
    }) as JugState["jugs"];

    newState.simple = this.getUniqueStringOutOfState(newState);
    return newState;
  }

  transfer(state: JugState, target: Jug["name"]): JugState {
    const newState = dangerousDeepClone(state);
    newState.action =
      target === "small" ? STATE.TRANSFER_SMALL : STATE.TRANSFER_LARGE;

    const [small, large] = newState.jugs;

    let [from, to] = target === "small" ? [small, large] : [large, small];

    const toAvailability = to.capacity - to.value;
    to.value = Math.min(to.value + from.value, to.capacity);
    from.value = Math.max(from.value - toAvailability, 0);

    newState.simple = this.getUniqueStringOutOfState(newState);
    return newState;
  }

  getUniqueStringOutOfState(state: JugState) {
    return `${state.jugs[0].value},${state.jugs[1].value}`;
  }

  buildPathForState(parent: JugState, child: JugState) {
    const found = this.pathList.find((states) => {
      const lastIndex = states[states.length - 1];
      return (lastIndex as JugState).simple === parent.simple;
    });

    if (found) {
      found.push(child);
    } else {
      const foundSecondFromLast = this.pathList.find((states) => {
        const secondFromLast = states[states.length - 2];
        return (secondFromLast as JugState).simple === parent.simple;
      });

      if (foundSecondFromLast) {
        this.pathList.push([...foundSecondFromLast.slice(0, -1), child]);
      } else {
        this.pathList.push([parent, child]);
      }
    }
  }

  // Basically if any of the jugs is equal to the desired amount or the combination of both problem is solved.
  stateHasGoal(state: JugState): boolean {
    const small = state.jugs[0].value;
    const large = state.jugs[1].value;
    return (
      [small, large].includes(this.zGallon) || small + large === this.zGallon
    );
  }

  solveHillClimbing(): JugState[] | typeof NO_SOLUTION {
    if (!this.validateInstance()) {
      return NO_SOLUTION;
    }

    while (this.queue.length) {
      const current = this.queue.pop() as JugState;

      if (this.stateHasGoal(current)) {
        return this.pathList.find(
          (path) => path[path.length - 1].simple === current.simple
        ) as JugState[];
      }

      const nextStates = [
        this.fillJug(current, "small"),
        this.fillJug(current, "large"),
        this.emptyJug(current, "small"),
        this.emptyJug(current, "large"),
        this.transfer(current, "small"),
        this.transfer(current, "large"),
      ];

      let heuristicResults = [];

      for (let state of nextStates) {
        const seen = this.tree.has(state.simple);

        if (!seen) {
          heuristicResults.push({
            heuristicValue: this.heuristic(state),
            state: state,
          });
        }
      }

      // sort by heuristic value
      heuristicResults.sort((a, b) => a.heuristicValue - b.heuristicValue);
      const nextState = heuristicResults[0].state;

      this.addEdge(current.simple, nextState.simple);
      this.buildPathForState(current, nextState);
      this.queue.push(nextState);
    }

    return NO_SOLUTION;
  }

  //Backtracking solution with recursion.
  solveBKT(state: JugState = this.queue[0]) {
    if (this.stateHasGoal(state)) {
      return this.pathList.find(
        (path) => path[path.length - 1].simple === state.simple
      ) as JugState[];
    }

    const current = this.queue.pop() as JugState;

    const nextStates = [
      this.fillJug(current, "small"),
      this.fillJug(current, "large"),
      this.emptyJug(current, "small"),
      this.emptyJug(current, "large"),
      this.transfer(current, "small"),
      this.transfer(current, "large"),
    ];

    for (let state of nextStates) {
      const seen = this.tree.has(state.simple);

      if (!seen) {
        this.addEdge(current.simple, state.simple);
        this.buildPathForState(current, state);
        this.queue.push(state);

        this.solveBKT(state);
      }
    }
  }

  validateInstance(
    xGallon = this.xGallon,
    yGallon = this.yGallon,
    zGallon = this.zGallon
  ): boolean {
    const gcd = (a: number, b: number): number => {
      if (b === 0) return a;
      return gcd(b, a % b);
    };

    const gcdAB = gcd(xGallon, yGallon);

    return zGallon % gcdAB === 0 && zGallon <= xGallon + yGallon;
  }

  solveBFS(): JugState[] | typeof NO_SOLUTION {
    if (!this.validateInstance()) {
      return NO_SOLUTION;
    }

    while (this.queue.length) {
      const current = this.queue.shift() as JugState;

      const nextStates = [
        this.fillJug(current, "small"),
        this.fillJug(current, "large"),
        this.emptyJug(current, "small"),
        this.emptyJug(current, "large"),
        this.transfer(current, "small"),
        this.transfer(current, "large"),
      ];

      for (let state of nextStates) {
        const seen = this.tree.has(state.simple);

        if (!seen) {
          this.addEdge(current.simple, state.simple);
          this.buildPathForState(current, state);
          this.queue.push(state);
        }

        if (this.stateHasGoal(state)) {
          return this.pathList.find(
            (path) => path[path.length - 1].simple === state.simple
          ) as JugState[];
        }
      }
    }
    return NO_SOLUTION;
  }

  solveAStar(): JugState[] | typeof NO_SOLUTION {
    if (!this.validateInstance()) {
      return NO_SOLUTION;
    }

    const heuristicResults = this.generateNextStates(
      this.queue.shift() as JugState
    );

    for (let res of heuristicResults) {
      this.queue.push(res.state);
    }

    while (this.queue.length) {
      const current = this.queue.shift() as JugState;

      if (this.stateHasGoal(current)) {
        return this.pathList.find(
          (path) => path[path.length - 1].simple === current.simple
        ) as JugState[];
      }

      const neighborHeuristicResults = this.generateNextStates(current);

      for (let res of neighborHeuristicResults) {
        const seen = this.queue.includes(res.state);
        if (!seen) {
          continue;
        }
      }

      // for (let state of nextStates) {
      //   const seen = this.tree.has(state.simple);

      //   if (!seen) {
      //     this.addEdge(current.simple, state.simple);
      //     this.buildPathForState(current, state);
      //     this.queue.push(state);
      //   }

      //   const neighbors = [
      //     this.fillJug(state, "small"),
      //     this.fillJug(state, "large"),
      //     this.emptyJug(state, "small"),
      //     this.emptyJug(state, "large"),
      //     this.transfer(state, "small"),
      //     this.transfer(state, "large"),
      //   ];

      //   for (let neighbor of neighbors) {
      //     const seen = this.tree.has(neighbor.simple);

      //     if (!seen) {
      //       this.addEdge(state.simple, neighbor.simple);
      //       this.buildPathForState(state, neighbor);
      //       this.queue.push(neighbor);
      //     }
      //   }
      // }
    }

    return NO_SOLUTION;
  }

  // TODO: Add interface for heuristic results
  generateNextStates(current: JugState) {
    const nextStates = [
      this.fillJug(current, "small"),
      this.fillJug(current, "large"),
      this.emptyJug(current, "small"),
      this.emptyJug(current, "large"),
      this.transfer(current, "small"),
      this.transfer(current, "large"),
    ];

    let heuristicResults = [];

    for (let state of nextStates) {
      const seen = this.tree.has(state.simple);

      if (!seen) {
        heuristicResults.push({
          heuristicValue: this.heuristic(state),
          state: state,
        });
      }
    }

    // sort by heuristic value
    heuristicResults.sort((a, b) => a.heuristicValue - b.heuristicValue);
    return heuristicResults;
  }

  heuristic(state: JugState): number {
    const [smallCapacity, largeCapacity] = [this.xGallon, this.yGallon].sort(
      (a, b) => a - b
    );
    const [small, large] = [state.jugs[0], state.jugs[1]].sort(
      (a, b) => a.value - b.value
    );

    const smallProd = smallCapacity * small.value;
    const largeProd = largeCapacity * large.value;

    return smallProd + largeProd;
  }
}

export interface Capacity {
  A: number;
  B: number;
}

export class WaterJugProblem {
  final: number;
  capacities: Capacity;
  states: number[][] = [];

  constructor(final: number, capacities: Capacity) {
    this.final = final;
    this.capacities = capacities;
    this.init();
  }

  init() {
    this.states = [[0, 0]];
  }

  isStateExist(state: number[]) {
    return this.states.some((s) => s[0] === state[0] && s[1] === state[1]);
  }

  checkFinalState(state: number[]) {
    return state[0] === this.final || state[1] === this.final;
  }

  fillA(state: number[]) {
    return [this.capacities.A, state[1]];
  }

  fillB(state: number[]) {
    return [state[0], this.capacities.B];
  }

  emptyA(state: number[]) {
    return [0, state[1]];
  }

  emptyB(state: number[]) {
    return [state[0], 0];
  }

  //Refactor
  pourAtoB(state: number[]) {
    const amount = Math.min(state[0], this.capacities.B - state[1]);
    return [state[0] - amount, state[1] + amount];
  }

  pourBtoA(state: number[]) {
    const amount = Math.min(state[1], this.capacities.A - state[0]);
    return [state[0] + amount, state[1] - amount];
  }

  solve() {
    let i = 0;
    while (i < this.states.length) {
      const state = this.states[i];

      if (this.checkFinalState(state)) {
        return state;
      }

      const actions = [
        this.fillA(state),
        this.fillB(state),
        this.emptyA(state),
        this.emptyB(state),
        this.pourAtoB(state),
        this.pourBtoA(state),
      ];

      for (const action of actions) {
        if (!this.isStateExist(action)) {
          this.states.push(action);
          break;
        }
      }

      i++;
    }
  }

  getShortestPath() {
    const queue: number[][][] = [];

    queue.push(this.states);

    while (queue.length > 0) {
      const lastPath = queue.shift() as number[][];
      const lastState = lastPath[(lastPath?.length as number) - 1];

      if (this.checkFinalState(lastState)) {
        return lastPath;
      }

      const actions = [
        this.fillA(lastState),
        this.fillB(lastState),
        this.emptyA(lastState),
        this.emptyB(lastState),
        this.pourAtoB(lastState),
        this.pourBtoA(lastState),
      ];

      actions.forEach((action) => {
        if (!this.isStateExist(action)) {
          this.states.push(action);
          queue.push(this.states);
        }
      });
    }
  }
}

const capacities: Capacity = {
  A: 9,
  B: 4,
};

const problem = new WaterJugProblem(6, capacities);
// problem.solve();
// console.log(problem.states[problem.states.length - 1]);

problem.solve();
console.log(problem.states);

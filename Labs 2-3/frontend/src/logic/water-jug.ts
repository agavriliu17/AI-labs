import { Capacity } from "./interfaces";

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

  solveGreedy() {
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

  solveBFS() {
    //BFS algorithm here
  }

  solveBacktracking() {
    //Backtracking algorithm here
  }

  validate(final: number, capacities: Capacity) {
    const gcd = (a: number, b: number): number => {
      if (b === 0) return a;
      return gcd(b, a % b);
    };

    const gcdAB = gcd(capacities.A, capacities.B);

    return final % gcdAB === 0 && final <= capacities.A + capacities.B;
  }
}

// const capacities: Capacity = {
//   A: 9,
//   B: 4,
// };

// const problem = new WaterJugProblem(6, capacities);

// problem.solveGreedy();
// console.log(problem.states);

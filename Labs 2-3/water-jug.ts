const enum CAPACITY {
  A = 9,
  B = 4,
}

class WaterJugProblem {
  final: number;
  capacities: CAPACITY;
  states: number[][];

  constructor(final: number, capacities: CAPACITY) {
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
}

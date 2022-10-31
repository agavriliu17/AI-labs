export interface Jug {
  value: number;
  readonly capacity: number;
  readonly name: "small" | "large";
}

export interface JugState {
  action: string;
  simple: string;
  jugs: [Jug, Jug];
}

export interface HeuristicResult {
  state: JugState;
  value: number;
}

export interface UserInput {
  first: number;
  second: number;
  final: number;
}

export enum Strategies {
  BFS = "BFS",
  BKTR = "Backtracking",
  HillClimbing = "Hill Climbing",
  AStar = "A*",
}

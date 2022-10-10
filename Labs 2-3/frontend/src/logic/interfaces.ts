export interface UserInput {
  first: number;
  second: number;
  final: number;
}

export enum Strategies {
  Greedy = "Greedy",
  BFS = "BFS",
  BKTR = "Backtracking",
  HillClimbing = "Hill Climbing",
  AStar = "A*",
}

export interface Capacity {
  A: number;
  B: number;
}

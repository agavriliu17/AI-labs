import { WaterJugProblem, Capacity } from "./water-jug";

const capacities: Capacity = {
  A: 9,
  B: 4,
};

const problem = new WaterJugProblem(6, capacities);

console.log(problem.solve());

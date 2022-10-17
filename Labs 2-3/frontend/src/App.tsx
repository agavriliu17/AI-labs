import { useState } from "react";
import Sheet from "@mui/joy/Sheet";
import Typography from "@mui/joy/Typography";
import { CssVarsProvider } from "@mui/joy/styles";

import FormControl from "@mui/joy/FormControl";
import FormLabel from "@mui/joy/FormLabel";
import Radio from "@mui/joy/Radio";
import RadioGroup from "@mui/joy/RadioGroup";
import Input from "@mui/joy/Input";
import Button from "@mui/joy/Button";
import { UserInput, Strategies } from "./logic/interfaces";
import ResultsModal from "./Modal";
import { WaterJugSolver } from "./logic/water-jug-solver";

function App() {
  const [inputs, setInputs] = useState<UserInput>({
    first: 0,
    second: 0,
    final: 0,
  });
  const [strategy, setStrategy] = useState<Strategies>(Strategies.BFS);
  const [problem, setProblem] = useState<WaterJugSolver | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [open, setOpen] = useState(false);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setInputs({ ...inputs, [name]: value });
  };

  const handleStrategyChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setStrategy(event.target.value as Strategies);
  };

  const handleSubmit = () => {
    const { first, second, final } = inputs;
    const solver = new WaterJugSolver(first, second, final);

    try {
      switch (strategy) {
        case Strategies.BFS:
          solver.solveBFS();
          break;
        case Strategies.BKTR:
          solver.solveBFS();
          break;
        default:
          break;
      }
      setProblem(solver);
      setOpen(true);
    } catch (e) {
      setError(
        "Seems like it's not possible to solve this problem with given inputs"
      );
    }
  };

  const handleModalClose = () => setOpen(false);

  const disabledButton = !inputs.first || !inputs.second || !inputs.final;
  return (
    <CssVarsProvider>
      <Sheet
        sx={{
          width: "100vw",
          height: "100vh",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography level="h1">Water-Jug Problem</Typography>

        <Typography
          sx={{ width: "50%", marginTop: "3rem" }}
          level="h6"
          textAlign="center"
        >
          We have two containers of capacity X liters and Y liters respectively
          and an unlimited amount of water. Let's determine a sequence of
          filling the containers and pouring from one container into the other
          (until it is full) or on the ground, so that Z liters remain in one of
          the containers. We have no other method of measuring a quantity of
          water.
        </Typography>

        <Sheet
          sx={{
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
            padding: "1rem 20rem",
            marginTop: "2rem",
            gap: "5rem",
          }}
        >
          <Sheet>
            <FormControl>
              <FormLabel sx={{ fontSize: "16px" }}>First bucket</FormLabel>
              <Input
                placeholder="X liters"
                type="number"
                variant="soft"
                value={inputs.first === 0 ? "" : inputs.first}
                onChange={handleInputChange}
                name="first"
              />
            </FormControl>

            <FormControl>
              <FormLabel sx={{ marginTop: "10px", fontSize: "16px" }}>
                Second bucket
              </FormLabel>
              <Input
                placeholder="Y liters"
                type="number"
                variant="soft"
                value={inputs.second === 0 ? "" : inputs.second}
                onChange={handleInputChange}
                name="second"
              />
            </FormControl>

            <FormControl>
              <FormLabel sx={{ marginTop: "10px", fontSize: "16px" }}>
                Desired quantity
              </FormLabel>
              <Input
                placeholder="Z liters"
                type="number"
                variant="soft"
                value={inputs.final === 0 ? "" : inputs.final}
                onChange={handleInputChange}
                name="final"
              />
            </FormControl>
          </Sheet>

          <FormControl>
            <Sheet>
              <FormLabel sx={{ fontSize: "16px" }}>Strategy</FormLabel>
              <RadioGroup
                defaultValue="greedy"
                name="controlled-radio-buttons-group"
                value={strategy}
                onChange={handleStrategyChange}
                sx={{ my: 1 }}
              >
                <Radio
                  value={Strategies.BFS}
                  label={Strategies.BFS}
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value={Strategies.BKTR}
                  label={Strategies.BKTR}
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value={Strategies.HillClimbing}
                  label={Strategies.HillClimbing}
                  disabled
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value={Strategies.AStar}
                  label={Strategies.AStar}
                  disabled
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
              </RadioGroup>
            </Sheet>
          </FormControl>
        </Sheet>

        <Button
          onClick={handleSubmit}
          variant="soft"
          sx={{ marginTop: "2rem" }}
          disabled={disabledButton}
        >
          Calculate
        </Button>

        {error && (
          <Typography sx={{ marginTop: "2rem" }} level="h6" color="danger">
            {error}
          </Typography>
        )}

        <ResultsModal
          open={open}
          onClose={handleModalClose}
          problem={problem}
          type={strategy}
        />
      </Sheet>
    </CssVarsProvider>
  );
}

export default App;

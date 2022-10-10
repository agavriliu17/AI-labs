import React from "react";
import Sheet from "@mui/joy/Sheet";
import Typography from "@mui/joy/Typography";
import { CssVarsProvider } from "@mui/joy/styles";

import FormControl from "@mui/joy/FormControl";
import FormLabel from "@mui/joy/FormLabel";
import Radio from "@mui/joy/Radio";
import RadioGroup from "@mui/joy/RadioGroup";
import Input from "@mui/joy/Input";
import Button from "@mui/joy/Button";

function App() {
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
          <FormControl>
            <FormLabel sx={{ fontSize: "16px" }}>First bucket</FormLabel>
            <Input placeholder="X liters" type="number" variant="soft" />

            <FormLabel sx={{ marginTop: "10px", fontSize: "16px" }}>
              Second bucket
            </FormLabel>
            <Input placeholder="Y liters" type="number" variant="soft" />

            <FormLabel sx={{ marginTop: "10px", fontSize: "16px" }}>
              Desired quantity
            </FormLabel>
            <Input placeholder="Z liters" type="number" variant="soft" />
          </FormControl>

          <FormControl>
            <Sheet>
              <FormLabel sx={{ fontSize: "16px" }}>Strategy</FormLabel>
              <RadioGroup
                defaultValue="greedy"
                name="controlled-radio-buttons-group"
                // value={value}
                // onChange={handleChange}
                sx={{ my: 1 }}
              >
                <Radio
                  value="greedy"
                  label="Greedy"
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value="bfs"
                  label="BFS"
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value="bktr"
                  label="Backtracking"
                  disabled
                  sx={{ marginTop: "15px" }}
                  color="primary"
                  variant="soft"
                />
                <Radio
                  value="hillClimb"
                  label="Hill Climbing"
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
          onClick={function () {}}
          variant="soft"
          sx={{ marginTop: "2rem" }}
        >
          Calculate
        </Button>
      </Sheet>
    </CssVarsProvider>
  );
}

export default App;

import React, { FC, Fragment } from "react";
import { Strategies } from "./logic/interfaces";

import Button from "@mui/joy/Button";
import Modal from "@mui/joy/Modal";
import ModalClose from "@mui/joy/ModalClose";
import ModalDialog from "@mui/joy/ModalDialog";
import Typography from "@mui/joy/Typography";
import { WaterJugSolver } from "./logic/water-jug-solver";
import Sheet from "@mui/joy/Sheet";

interface Props {
  open: boolean;
  type: Strategies;
  problem: WaterJugSolver | null;
  onClose: () => void;
}

const ResultsModal: FC<Props> = ({ type, problem, onClose, open }) => {
  return (
    <Modal open={open} onClose={onClose}>
      <ModalDialog
        aria-labelledby="layout-modal-title"
        aria-describedby="layout-modal-description"
        layout="center"
        sx={{ padding: "2rem", maxWidth: "540px" }}
      >
        <ModalClose />
        <Typography
          id="layout-modal-title"
          component="h2"
          level="inherit"
          fontSize="1.5em"
          mb="0.25em"
        >
          Results
        </Typography>
        <Typography textColor="text.tertiary">Algorithm: {type}</Typography>
        <Typography textColor="text.tertiary" mt="10px">
          First bucket capacity: {problem?.xGallon} liters
        </Typography>
        <Typography textColor="text.tertiary">
          Second bucket capacity: {problem?.yGallon} liters
        </Typography>
        <Typography textColor="text.tertiary">
          Desired quantity: {problem?.zGallon} liters
        </Typography>

        <Typography mt="20px" textAlign="center" fontWeight="600">
          Steps
        </Typography>
        <Sheet
          sx={{
            display: "flex",
            flexDirection: "row",
            flexWrap: "wrap",
            justifyContent: "center",
          }}
        >
          {/* {problem?.states.map((state, index) => (
            <Fragment key={index}>
              <Typography
                textColor={
                  index !== problem?.states.length - 1
                    ? "text.tertiary"
                    : "text.primary"
                }
                m={1}
              >
                {`[${state[0]}, ${state[1]}]`}
              </Typography>
              {index !== problem?.states.length - 1 && (
                <Typography textColor="text.tertiary" m={1}>
                  {"=>"}
                </Typography>
              )}
            </Fragment>
          ))} */}
        </Sheet>

        <Sheet
          sx={{
            width: "100%",
            display: "flex",
            justifyContent: "center",
            marginTop: "1rem",
          }}
        >
          <Button onClick={onClose} variant="soft">
            Done
          </Button>
        </Sheet>
      </ModalDialog>
    </Modal>
  );
};

export default ResultsModal;

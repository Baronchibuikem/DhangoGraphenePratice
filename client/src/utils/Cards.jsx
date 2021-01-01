import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";
import Avatar from "@material-ui/core/Avatar";
import { red } from "@material-ui/core/colors";
import Button from "@material-ui/core/Button";

import Modal from "./Modal";

const useStyles = makeStyles((theme) => ({
  root: {
    maxWidth: 345,
  },
  media: {
    height: 0,
    paddingTop: "56.25%", // 16:9
  },
  expand: {
    transform: "rotate(0deg)",
    marginLeft: "auto",
    transition: theme.transitions.create("transform", {
      duration: theme.transitions.duration.shortest,
    }),
  },
  expandOpen: {
    transform: "rotate(180deg)",
  },
  avatar: {
    backgroundColor: red[500],
  },
}));

export const GenericCard = (props) => {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardHeader
        avatar={
          <Avatar aria-label="recipe" className={classes.avatar}>
            RC
          </Avatar>
        }
        // action={
        //   <IconButton aria-label="settings">
        //     <MoreVertIcon />
        //   </IconButton>
        // }
        title={props.rider}
        subheader={props.created}
      />
      <div className="row">
        <div className="col-md-6">
          <CardContent>
            <h6 className="text-center text-bold mt-2">{props.status}</h6>
          </CardContent>
        </div>
        <div className="col-md-6">
          <CardActions>
            <Button
              variant="contained"
              color="primary"
              className="mx-auto"
              data-toggle="modal"
              data-target={`#${props.id}`}
            >
              View details
            </Button>

            <Modal
              id={props.id}
              name={props.rider}
              status={props.status}
              from={props.from}
              to={props.to}
              created={props.created}
            />
          </CardActions>
        </div>
      </div>
    </Card>
  );
};

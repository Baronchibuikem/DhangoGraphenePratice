import React from "react";
import { Route, Switch } from "react-router-dom";
import Login from "./components/Authentication/Login";
import Signup from "./components/Authentication/Signup";
import Driver from "./components/Dashboard/DriverDashboard";
import Rider from "./components/Dashboard/RiderDashboard";

const BaseRouter = () => (
  <Switch>
    <Route exact path="/log-in" component={Login} />
    <Route exact path="/sign-up" component={Signup} />
    <Route exact path="/driver-dashboard" component={Driver} />
    <Route exact path="/rider-dashboard" component={Rider} />

    {/* <PrivateRoute exact path="/:id" component={singlePoll} /> */}
  </Switch>
);
export default BaseRouter;

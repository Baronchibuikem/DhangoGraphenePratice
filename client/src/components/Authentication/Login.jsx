import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { useForm } from "react-hook-form";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import "../../assets/css/Login.css";
import { Link, Redirect } from "react-router-dom";
import { loginUser } from "../../store/actions/authActions";

export default function Login() {
  // Here we are instantiating our dispatch action
  const dispatch = useDispatch();

  // hooks form
  const { register, handleSubmit, errors } = useForm();

  // this is used to dispatch a redux action with the neeeded login data
  const loginSubmit = (data) => {
    dispatch(loginUser({ username: data.username, password: data.password }));
  };

  const params = useSelector((state) => ({
    errors: state.error_reducer.error,
    isAuthenticated: state.authentication.isAuthenticated,
    user: state.authentication.user,
  }));

  if (params.isAuthenticated === true && params.user.group === "Rider") {
    return <Redirect to="/rider-dashboard" />;
  }

  if (params.isAuthenticated === true && params.user.group === "Driver") {
    return <Redirect to="/driver-dashboard" />;
  }
  return (
    <div
      style={{
        // backgroundColor: "#282c34",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Card className="container col-md-5 py-5 col-sm-12">
        <form onSubmit={handleSubmit(loginSubmit)}>
          <CardContent>
            <Typography
              class="text-uppercase text-center font-weight-bold"
              style={{ fontSize: "20px" }}
            >
              Sign In <i className="fas fa-user mx-2"></i>
            </Typography>

            <input
              type="text"
              className="form-control p-4 w-100"
              placeholder="Username"
              name="username"
              ref={register({ required: true })}
            />
            <h6 className="text-left font-italic text-danger">
              {errors.username && errors.username.type === "required" && (
                <p>Username is required</p>
              )}
            </h6>
            <input
              type="password"
              className="form-control p-4 w-100"
              placeholder="Password"
              name="password"
              ref={register({ required: true })}
            />
            <h6 className="text-left font-italic text-danger">
              {errors.password && errors.password.type === "required" && (
                <p>Password field is required</p>
              )}
            </h6>
            <CardActions>
              <Button
                disableElevation
                className="mx-auto px-5 py-3 my-2 col-sm-12 text-light"
                type="submit"
                style={{ backgroundColor: "gray" }}
                fullWidth
              >
                Log in
              </Button>
            </CardActions>
            <h6 className="text-center">
              Don't have a registered account? Click{" "}
              <Link exact to="/sign-up">
                here
              </Link>{" "}
              to Register now
            </h6>
          </CardContent>
        </form>
      </Card>
    </div>
  );
}

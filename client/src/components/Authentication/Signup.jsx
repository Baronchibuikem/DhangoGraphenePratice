import React from "react";
import Typography from "@material-ui/core/Typography";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";

import "../../assets/css/Login.css";
import { Link, Redirect } from "react-router-dom";
import { useForm } from "react-hook-form";
import { registerUser } from "../../store/actions/authActions";
import { useSelector, useDispatch } from "react-redux";

export default function Register() {
  const { register, handleSubmit, errors, watch } = useForm();

  // Here we are instantiating our dispatch action
  const dispatch = useDispatch();

  // This is used to dispatch a redux action with the needed registration data
  const regSubmit = (data) => {
    console.log(data, "data from registration");
    dispatch(
      registerUser({
        data,
      })
    );
  };

  const params = useSelector((state) => ({
    authenticated: state.authentication.isAuthenticated,
  }));
  // Here we are checking if our authenticated value from the state is true, it yes we redirect to the homepage
  if (params.authenticated) {
    return <Redirect to="/" />;
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
      <Card className="container col-md-6  col-sm-12 sm-screen">
        <form onSubmit={handleSubmit(regSubmit)}>
          <CardContent>
            <Typography
              className="text-uppercase text-center font-weight-bold py-3"
              style={{ fontSize: "20px" }}
            >
              Sign up <i className="fas fa-user mx-2"></i>
            </Typography>
            {/* Enter your first name */}

            <div className="row">
              <div className="col-md-6 col-sm-12 my-2">
                <input
                  type="text"
                  className="form-control p-4 w-100"
                  placeholder="First name"
                  name="first_name"
                  ref={register({ required: true })}
                />
                <h6 className="text-left font-italic text-danger">
                  {errors.first_name &&
                    errors.first_name.type === "required" && (
                      <p>First name is required</p>
                    )}
                </h6>
              </div>
              <div className="col-md-6 col-sm-12 my-2">
                <input
                  type="text"
                  className="form-control p-4 w-100"
                  placeholder="Last Name"
                  name="last_name"
                  ref={register({ required: true })}
                />
                <h6 className="text-left font-italic text-danger">
                  {errors.last_name && errors.last_name.type === "required" && (
                    <p>Last name is required</p>
                  )}
                </h6>
              </div>
              <div className="col-md-6 col-sm-12 my-2">
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
              </div>
              <div className="col-md-6 col-sm-12 my-2">
                {/* User Role */}
                <select name="group" ref={register} className="form-control">
                  <option value="rider" className="form-control">
                    Rider
                  </option>
                  <option value="driver" className="form-control py-4">
                    Driver
                  </option>
                </select>
              </div>
              <div className="col-md-6 col-sm-12 my-2">
                <input
                  type="password"
                  className="form-control p-4 w-100"
                  placeholder="Password"
                  name="password1"
                  ref={register({ required: true })}
                />
                <h6 className="text-left font-italic text-danger">
                  {errors.password1 && errors.password1.type === "required" && (
                    <p>Password field is required</p>
                  )}
                </h6>
              </div>
              <div className="col-md-6 col-sm-12 my-2">
                <input
                  type="password"
                  className="form-control p-4 w-100"
                  placeholder="Confirm passowrd"
                  name="password2"
                  ref={register({
                    required: true,
                    validate: (value) => {
                      return value === watch("password1");
                    },
                  })}
                />
                <h6 className="text-left font-italic text-danger">
                  {errors.password2 && errors.password2.type === "required" && (
                    <p>Please confirm your password</p>
                  )}
                </h6>
                <h6 className="text-left font-italic text-danger">
                  {errors.password2 && errors.password2.type === "validate" && (
                    <p>Passwords don't match</p>
                  )}
                </h6>
              </div>
            </div>

            <Button
              disableElevation
              className="mx-auto px-5 py-3 my-2 col-sm-12 text-light"
              type="submit"
              style={{ backgroundColor: "gray" }}
              fullWidth
            >
              {/* {params.status ? (
                  <div>
                    <span>Loading</span>
                  </div>
                ) : (
                  "Register"
                )} */}
              Sign up
            </Button>
            <div className="mx-auto">
              <h6 className="text-center">
                Already registered? then click{" "}
                <Link to="/log-in" className="mx-auto">
                  here
                </Link>{" "}
                to Login now
              </h6>
            </div>
          </CardContent>
        </form>
      </Card>
    </div>
  );
}

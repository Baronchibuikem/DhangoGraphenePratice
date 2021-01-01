import setAuthToken from "../../utils/setAuthToken";
import jwt_decode from "jwt-decode";
import { route } from "../api_calls";
import { GET_ERRORS, SET_CURRENT_USER, SET_USER_TOKEN } from "./action_types";

let config = { headers: { "Content-Type": "application/json" } };

// Register User action
export const registerUser = (params) => async (dispatch) => {
  const {
    first_name,
    username,
    last_name,
    group,
    password1,
    password2,
  } = params.data;
  try {
    const response = await route.post("/account/register/", {
      first_name,
      username,
      last_name,
      group,
      password1,
      password2,
    });
    if (response) {
      console.log("response from reg", response);
      dispatch({ type: SET_CURRENT_USER, payload: response.data });
    }
  } catch (error) {
    dispatch({
      type: GET_ERRORS,
      payload: error && error.response && error.response.data,
    });
  }
};

// Login - Get User Token
export const loginUser = (userData) => async (dispatch) => {
  const { username, password } = userData;
  try {
    const res = await route.post(
      "/account/login/",
      { username, password },
      config.headers
    );
    if (res) {
      // Save to localStorage
      console.log(res.data, "response from login");
      const { access } = res.data;
      // Set token to local storage
      dispatch({ type: SET_USER_TOKEN, payload: access });
      // Decode token to get user data
      const decoded = jwt_decode(access);
      // Set current user
      dispatch(setCurrentUser(decoded));
    }
  } catch (err) {
    dispatch({
      type: GET_ERRORS,
      payload: err && err.response && err.response.data,
    });
  }
};

// Set logged in user
export const setCurrentUser = (decoded) => {
  console.log(decoded, "DECODED");
  return {
    type: SET_CURRENT_USER,
    payload: decoded,
  };
};

// Log user out
export const logoutUser = () => (dispatch) => {
  // Remove auth header for future requests
  setAuthToken(false);
  // Set current user to {} which will set isAuthenticated to false
  dispatch(setCurrentUser({}));
};

import setAuthToken from "../../utils/setAuthToken";
import jwt_decode from "jwt-decode";
import { route } from "../api_calls";
import axios from "axios";
import { GET_ERRORS, GET_TRIPS, GET_TRIP_ID } from "./action_types";

let config = { headers: { "Content-Type": "application/json" } };

// Get all trips
export const getTrips = () => async (dispatch, getState) => {
  const token = getState().authentication.token;
  console.log(token, "token");
  let config = {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  };
  try {
    const response = await route.get("/trip/", config);
    console.log(response, "loading trip in actions");
    if (response) {
      dispatch({ type: GET_TRIPS, payload: response.data.results });
    }
  } catch (error) {
    dispatch({
      type: GET_ERRORS,
      payload: error && error.response && error.response.data,
    });
  }
};

// Get all trips
export const getTripById = (params) => async (dispatch, getState) => {
  const token = getState().authentication.token;
  const userToken = (axios.defaults.headers.common["Authorization"] = token);
  const { id } = params;
  try {
    const response = await route.get(`/trip/${id}/`, userToken);
    if (response) {
      dispatch({ type: GET_TRIP_ID, payload: response.data.results });
    }
  } catch (error) {
    dispatch({
      type: GET_ERRORS,
      payload: error && error.response && error.response.data,
    });
  }
};

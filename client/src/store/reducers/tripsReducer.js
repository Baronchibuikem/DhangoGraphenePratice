import { GET_TRIPS, GET_TRIP_ID } from "../actions/action_types";

const initialState = {
  trips: [],
  trip: {},
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_TRIPS:
      return {
        ...state,
        trips: action.payload,
      };
    default:
      return state;
  }
}

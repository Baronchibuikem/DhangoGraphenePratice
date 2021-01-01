import React, { useEffect, useState } from "react";
import { Redirect } from "react-router-dom";
import { getTrips } from "../../store/actions/trips";
import { useSelector, useDispatch } from "react-redux";
import { GenericCard } from "../../utils/Cards";

function Rider() {
  const [trips, setTrips] = useState([]);

  const params = useSelector((state) => ({
    trips: state.trips.trips,
  }));

  const dispatch = useDispatch();
  useEffect(() => {
    // console.log("trip loaded in components");
    // const loadTrips = async () => {
    //   const response = await getTrips();
    //   setTrips(response.data);
    // };
    // loadTrips();
    dispatch(getTrips());
  }, [dispatch]);

  const getUserTrips = () => {
    setTrips(params.trips);
    trips.map((trip) => {
      return trip.drop_off_address;
    });
  };
  return (
    <div>
      {/* <h1 className="display-1 mt-5 pt-5">{() => getTrips()}</h1> */}
      <div className=" container mt-5 pt-5">
        <div className="row">
          {params.trips.map((trip) => {
            return (
              <div className="col-md-4">
                <GenericCard
                  rider={trip.rider}
                  created={trip.created}
                  status={trip.status}
                  id={trip.id}
                  from={trip.pick_up_address}
                  to={trip.drop_off_address}
                  // image={trip.rider.photo}
                />
                {/* <h1 className="display-1">{trip.driver}</h1> */}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

export default Rider;

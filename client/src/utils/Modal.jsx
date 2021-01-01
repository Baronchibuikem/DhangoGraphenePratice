import React from "react";

function Modal(props) {
  return (
    <div
      className="modal fade"
      id={`${props.id}`}
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalCenterTitle"
      aria-hidden="true"
    >
      <div className="modal-dialog modal-dialog-centered" role="document">
        <div className="modal-content">
          <div className="modal-header mx-auto">
            <h5 className="modal-title text-uppercase">{props.name}</h5>
          </div>
          <div className="container">
            <div className="modal-body">
              <p>
                <span className="text-capitalize">
                  <b>
                    <i>{props.name}</i>
                  </b>
                </span>{" "}
                just requested for a driver to take them from{" "}
                <b>
                  <i>{props.from}</i>
                </b>{" "}
                to their destination at{" "}
                <b>
                  <i>{props.to}</i>
                </b>
              </p>
            </div>
          </div>

          <div className="modal-footer">
            <small>
              <b>{props.id}</b>
            </small>

            <button
              type="button"
              className="btn btn-secondary"
              data-dismiss="modal"
            >
              Close
            </button>
            <button type="button" className="btn btn-primary">
              Accept Trip
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Modal;

import axios from "axios";

const baseURL = "http://127.0.0.1:8000/api/v1";
const accessToken = localStorage.getItem("token");

export const route = axios.create({
  baseURL: baseURL,
  timeout: 30000,
  headers: {
    Authorization: accessToken ? `Bearer ${accessToken}` : null,
    "Content-Type": "application/json",
    accept: "application/json",
  },
});

// route.interceptors.response.use(
//   (response) => response,
//   async (error) => {
//     const originalRequest = error.config;

//     // Prevent infinite loops
//     if (
//       error.response.status === 401 &&
//       originalRequest.url === baseURL + "token/refresh/"
//     ) {
//       window.location.href = "/log-in/";
//       return Promise.reject(error);
//     }

//     if (
//       error.response.status === 401 &&
//       error.response.statusText === "Unauthorized"
//     ) {
//       const refresh = localStorage.getItem("refresh");

//       if (refresh) {
//         const tokenParts = JSON.parse(atob(refresh.split(".")[1]));

//         // exp date in token is expressed in seconds, while now() returns milliseconds:
//         const now = Math.ceil(Date.now() / 1000);

//         if (tokenParts.exp > now) {
//           try {
//             const response = await route.post("/token/refresh/", {
//               refresh,
//             });
//             setNewHeaders(response);
//             originalRequest.headers["Authorization"] =
//               "JWT " + response.data.access;
//             return route(originalRequest);
//           } catch (error) {
//             console.log(error);
//           }
//         } else {
//           console.log("Refresh token is expired", tokenParts.exp, now);
//           window.location.href = "/log-in/";
//         }
//       } else {
//         console.log("Refresh token not available.");
//         window.location.href = "/log-in/";
//       }
//     }

//     // specific error handling done elsewhere
//     return Promise.reject(error);
//   }
// );

// export function setNewHeaders(response) {
//   route.defaults.headers["Authorization"] = "Bearer " + response.data.access;
//   localStorage.setItem("access", response.data.access);
//   localStorage.setItem("refresh", response.data.refresh);
// }

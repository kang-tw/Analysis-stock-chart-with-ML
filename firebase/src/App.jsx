import { RouterProvider, createBrowserRouter } from "react-router-dom"
import styled, { createGlobalStyle } from "styled-components";
import reset from "styled-reset";
import LogIn from "./routes/login";
import { useEffect, useState } from "react";
import { auth } from "./firebase";
import LoadingScreen from "./components/loading-screen";
import SignUp from "./routes/signup";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LogIn />
  },
  {
    path: "/signup",
    element: <SignUp />
  }
]);

const GlobalStyle = createGlobalStyle`
    ${reset};
  * {
    box-sizing: border-box;
  }
  body {
    background-color: #363c40;
    color: white;
    font-family: Arial, sans-serif;
  }
`;

const Wrapper = styled.div`
  height: 100vh;
  display: flex;
  justify-content: center;
`;

function App() {
  const [isLoading, setLoading] = useState(true);
  const init = async() => {
    await auth.authStateReady();
    setLoading(false);
  };
  useEffect(() => {
    init();
  }, []);
  return (
    <Wrapper>
      <GlobalStyle />
      {isLoading ? <LoadingScreen /> : <RouterProvider router={router} />}
    </Wrapper>
  )
}

export default App

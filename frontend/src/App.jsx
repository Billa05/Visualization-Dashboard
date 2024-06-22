import "./App.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Menu from "./components/Menu";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Content from "./components/Content";
import { ChartsDataProvider } from "./ChartsContextProvider";

function App() {
  const Layout = () => {
    return (
      <>
        <div className="main w-full">
          <Navbar />
          <div className="Container flex w-full">
            <div className="menuContainer border-r-2 border-gray h-screen">
              <Menu />
            </div>
            <div className="contentContainerr w-full h-screen">
              <Content/>
            </div>
          </div>
          <Footer />
        </div>
      </>
    );
  };

  return (
    <ChartsDataProvider>
    <Router>
      <Routes>
        <Route path="*" element={<Layout />} />
      </Routes>
    </Router>
    </ChartsDataProvider>
  );
}

export default App;
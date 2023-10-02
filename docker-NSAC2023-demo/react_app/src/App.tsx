import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom"
import { Template } from "./template/Template"
import { TaskFormPage } from "./pages/TaskFormPage"
import { TasksPage } from "./pages/TasksPage"
import { HomePage } from "./pages/HomePage"
import { Toaster } from "react-hot-toast"
import { FundamentalsPage } from "./pages/FundamentalsPage"
import { AboutUsPage } from "./pages/AboutUsPage"
import { ImagenSpectroscopyPage } from "./pages/ImagenSpectroscopyPage"

function App() {
  return (
    <BrowserRouter>
      <Template>
        <Routes>
          <Route path="/" element={<Navigate to="/home" />}></Route>
          <Route path="/home" element={<HomePage />}></Route>
          <Route path="/fundamentals" element={<FundamentalsPage />}></Route>
          <Route path="/imagen-spectroscopy" element={<ImagenSpectroscopyPage />}></Route>
          <Route path="/about-us" element={<AboutUsPage />}></Route>
          <Route path="/tasks" element={<TasksPage />}></Route>
          <Route path="/tasks/create" element={<TaskFormPage />}></Route>
          <Route path="/tasks/:id" element={<TaskFormPage />}></Route>
        </Routes>
        <Toaster />
      </Template>
    </BrowserRouter>
  )
}

App.propTypes = {}

export default App

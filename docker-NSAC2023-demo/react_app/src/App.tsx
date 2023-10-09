import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom"
import { Template } from "./template/Template"
import { Toaster } from "react-hot-toast"
import { Suspense, lazy } from "react"

// Importa las páginas usando import() para code-splitting
const HomePage = lazy(() => import('./pages/HomePage'));
const FundamentalsPage = lazy(() => import('./pages/FundamentalsPage'));
const ImagenSpectroscopyPage = lazy(() => import('./pages/ImagenSpectroscopyPage'));
const AboutUsPage = lazy(() => import('./pages/AboutUsPage'));
const TasksPage = lazy(() => import('./pages/TasksPage'));
const TaskFormPage = lazy(() => import('./pages/TaskFormPage'));

function App() {
  return (
    <BrowserRouter>
      <Template>
        <Routes>
          <Route path="/" element={<Navigate to="/home" />} />
          <Route path="/home" element={<Suspense fallback={<div>Loading...</div>}><HomePage /></Suspense>} />
          <Route path="/fundamentals" element={<Suspense fallback={<div>Loading...</div>}><FundamentalsPage /></Suspense>} />
          <Route path="/imagen-spectroscopy" element={<Suspense fallback={<div>Loading...</div>}><ImagenSpectroscopyPage /></Suspense>} />
          <Route path="/about-us" element={<Suspense fallback={<div>Loading...</div>}><AboutUsPage /></Suspense>} />
          <Route path="/tasks" element={<Suspense fallback={<div>Loading...</div>}><TasksPage /></Suspense>} />
          <Route path="/tasks/create" element={<Suspense fallback={<div>Loading...</div>}><TaskFormPage /></Suspense>} />
          <Route path="/tasks/:id" element={<Suspense fallback={<div>Loading...</div>}><TaskFormPage /></Suspense>} />
        </Routes>
        <Toaster />
      </Template>
    </BrowserRouter>
  );
}

App.propTypes = {}

export default App

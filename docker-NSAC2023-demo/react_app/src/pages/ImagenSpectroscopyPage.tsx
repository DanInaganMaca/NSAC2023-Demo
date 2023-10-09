import { Col } from "antd";
import { ContentPage } from "../components/ContentPage";
import { ImageHeader } from "../components/ImageHeader";
import header from "../assets/spectrumcopy.png"


export default function ImagenSpectroscopyPage() {
  return (
    <Col span={24} style={{ background: "#001529" }}>
      <ImageHeader img={header} />
      <div style={{ textAlign: "center", color: "white" }}>
        <h1>Image Spectroscopy</h1>
      </div>
      <ContentPage key={'imageSpectroscopy'} code={'imageSpectroscopy'} />
    </Col>
  )
}

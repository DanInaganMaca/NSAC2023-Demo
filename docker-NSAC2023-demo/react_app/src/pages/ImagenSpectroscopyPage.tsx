import { Col } from "antd";
import { ContentPage } from "../components/ContentPage";
import { ImageHeader } from "../components/ImageHeader";
import header from "../assets/spectrumcopy.png"


export function ImagenSpectroscopyPage() {
  return (
    <Col span={24}>
      <ImageHeader img={header} />
      <ContentPage key={'fundamentals'} code={'fundamentals'} />
    </Col>
  )
}

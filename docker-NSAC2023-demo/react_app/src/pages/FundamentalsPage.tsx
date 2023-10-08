import { Col } from "antd";
import { ContentPage } from "../components/ContentPage";
import { ImageHeader } from "../components/ImageHeader";
import header from "../assets/imageHeaderFundamentals.png"


export function FundamentalsPage() {
  return (
    <Col span={24} style={{ background: "#001529" }}>
      <ImageHeader img={header} />
      <div style={{ textAlign: "center", color: "white" }}>
        <h1>Fundamentals</h1>
      </div>
      <ContentPage key={'fundamentals'} code={'fundamentals'} />
    </Col>
  )
}

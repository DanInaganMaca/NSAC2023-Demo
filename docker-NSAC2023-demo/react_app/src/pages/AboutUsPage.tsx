import { Col } from "antd";
import { ContentPage } from "../components/ContentPage";

export function AboutUsPage() {
  return (
    <Col span={24} style={{ background: "#001529" }}>
      <div style={{ textAlign: "center", color: "white" }}>
        <h1>About Us</h1>
      </div>
      <ContentPage key={'aboutUs'} code={'aboutUs'} />
    </Col>
  )
}

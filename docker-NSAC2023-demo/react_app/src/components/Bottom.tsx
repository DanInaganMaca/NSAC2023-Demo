import { Col, Row } from "antd";
import logo from "../assets/logo.png"

export function Bottom() {
  return (
    <Row justify={"center"} align={"top"}>
      <Col span={6}>
        <InformationProjectComponent />
      </Col>
      <Col span={6}>
        <AboutUsComponent />
      </Col>
      <Col span={6}>
        <InformationChallengeComponent />
      </Col>
      <Col span={6}>
        <ContactUsComponent />
      </Col>
    </Row>
  )
}

function InformationProjectComponent() {
  return (
    <div>
      <Row justify={"center"}>
        <h4>
          Spectrum4Bio
        </h4>
      </Row>
      <Row justify={"center"}>
        <img src={logo} alt={"Spectrum4Bio"} width={"100px"} />
      </Row>
    </div>
  )
}

function AboutUsComponent() {
  return (
    <div>
      <Row justify={"center"}>
        <h5>
          About Us
        </h5>
      </Row>
    </div>
  )
}

function InformationChallengeComponent() {
  return (
    <div>
      <Row justify={"center"}>
        <h5>
          Space Apps Challenge
        </h5>
      </Row>
    </div>
  )
}

function ContactUsComponent() {
  return (
    <div>
      <Row justify={"center"}>
        <h5>
          Contact Us
        </h5>
      </Row>
    </div>
  )
}

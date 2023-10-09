import { Col, Row } from "antd";
import header from "../assets/photos.jpeg"
import { ImageHeader } from "../components/ImageHeader";

export default function AboutUsPage() {
  return (
    <Col span={24} style={{ background: "#001529" }}>
      <ImageHeader img={header} />
      <div style={{ textAlign: "center", color: "white" }}>
        <h1>About Us</h1>
      </div>
      <CorreosComponenta />
    </Col>
  )
}

const correos = [
  "daniloinagan@unicauca.edu.co",
  "gadiaz@unicauca.edu.co",
  "erikaluna1999@unicauca.edu.co",
  "jefryn@unicauca.edu.co",
  "y.carolmosquera@gmail.com",
  "fernandacar@unicauca.edu.co"
]

function CorreosComponenta() {
  return (
    <Row justify={"center"}>
      <Col>
        {
          correos && correos.map((correo) => {
            return (
              <Row>
                <h5 style={correoStyle}>{correo}</h5>
              </Row>
            )
          })
        }
      </Col>
    </Row>
  )
}

const correoStyle: React.CSSProperties = {
  color: "gray",
}

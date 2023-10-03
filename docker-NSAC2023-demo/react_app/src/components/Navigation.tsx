import { Button, Col, Menu, Row } from "antd";
import { HomeFilled, AppstoreAddOutlined, BuildOutlined, TeamOutlined } from '@ant-design/icons';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import { useNavigate } from "react-router-dom";
import logo from "../assets/logo.png"

export function Navigation() {
  const navigate = useNavigate();

  return (
    <Col span={24} style={{ maxWidth: "1920px" }}>
      <Row justify={'space-between'} align={"middle"}>
        <Col span={2}>
          <Button type="link" style={{ display: "flex", alignItems: "center", color: 'white', }} onClick={() => {
            navigate("/home");
          }}>
            <img src={logo} alt={"Spectrum4Bio"} width={"50px"} />
            <h4>Spectrum4Bio</h4>
          </Button>
        </Col>
        <Col span={21}>
          <Row justify={"end"}>
            <Menu
              theme="dark"
              mode={'horizontal'}
            >
              <Col span={24}>
                <Row justify={"center"} align={'middle'}>
                  <Col>
                    <Button type="link" style={{ color: 'white' }}
                      onClick={() => {
                        navigate("/home");
                      }}>
                      <HomeFilled />
                      Home</Button>
                  </Col>
                  <Col>
                    <Button type="link" style={{ color: 'white' }} onClick={() => {
                      navigate("/fundamentals");
                    }}>
                      <BuildOutlined />
                      Fundamentals</Button>
                  </Col>
                  <Col>
                    <Button type="link" style={{ color: 'white' }} onClick={() => {
                      navigate("/imagen-spectroscopy")
                    }}>
                      <AppstoreAddOutlined />
                      Imagen Spectroscopy</Button>
                  </Col>
                  <Col>
                    <Button type="link" style={{ color: 'white' }} onClick={() => {
                      navigate("/about-us");
                    }}>
                      <TeamOutlined />
                      About us</Button>
                  </Col>
                </Row>
              </Col>
            </Menu>
          </Row>
        </Col>
        <Col span={1} style={{ width: '100px' }}>
          <Row justify={"end"}>
            <a href="https://github.com/DanInaganMaca/NSAC2023-Demo" target="_blank" rel="noreferrer">
              <FontAwesomeIcon icon={faGithub} size="2xl" />
            </a>
          </Row>
        </Col>
      </Row>
    </Col>
  )
}

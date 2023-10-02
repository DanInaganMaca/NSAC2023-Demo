import { Layout, theme } from "antd";
import { Navigation } from "../components/Navigation";
import { ReactNode } from "react"; // Importa ReactNode

const { Header, Content, Footer } = Layout;

interface TemplateProps {
  children: ReactNode; // Define el tipo de children como ReactNode
}

export function Template({ children }: TemplateProps) {
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  return (
    <Layout className="layout">
      <Header style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
        <Navigation />
      </Header>
      <Content style={{ display: 'flex', justifyContent: 'center', alignItems: "center" }}>
        <div className="site-layout-content" style={{ background: colorBgContainer, width: "100%", maxWidth: "1920px" }}>
          {children} {/* Rederizar los componentes secundarios, el contenido */}
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>Ant Design ©2023 Created by Ant UED</Footer>
    </Layout >
  )
}

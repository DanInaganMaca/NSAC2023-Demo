import { Breadcrumb, Layout, Menu, theme } from "antd";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import { TasksPage } from "../pages/TasksPage";
import { TaskFormPage } from "../pages/TaskFormPage";
import { Toaster } from "react-hot-toast";
import { HomePage } from "../pages/HomePage";

const { Header, Content, Footer } = Layout;


export function Template() {
  const {
    token: { colorBgContainer },
  } = theme.useToken();

  return (
    <Layout className="layout">
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <div className="demo-logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['2']}
          items={new Array(15).fill(null).map((_, index) => {
            const key = index + 1;
            return {
              key,
              label: `nav ${key}`,
            };
          })}
        />
      </Header>
      <Content style={{ padding: '0 50px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
        <div className="site-layout-content" style={{ background: colorBgContainer }}>
          <BrowserRouter>
            <div className="container mx-auto">
              <Routes>
                <Route path="/" element={<Navigate to="/home" />}></Route>
                <Route path="/home" element={<HomePage />}></Route>
                <Route path="/tasks" element={<TasksPage />}></Route>
                <Route path="/tasks/create" element={<TaskFormPage />}></Route>
                <Route path="/tasks/:id" element={<TaskFormPage />}></Route>
              </Routes>
              <Toaster />
            </div>
          </BrowserRouter>
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>Ant Design ©2023 Created by Ant UED</Footer>
    </Layout>
  )
}

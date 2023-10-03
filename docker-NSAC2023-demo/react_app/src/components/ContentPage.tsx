import React, { useEffect, useState } from "react"
import { IPage, IContent } from "../models/pages.model";
import { getOne } from "../api/pages.api";
import { Col, Row } from "antd";

type ContentPageProps = {
  code: string
}

export function ContentPage({ code }: ContentPageProps) {

  const [contents, setContents] = useState<IContent[] | undefined>([]);

  useEffect(() => {
    const loadPage = async () => {
      try {
        const res = await getOne(code);
        const pageData: IPage = res.data;
        const contentsData: IContent[] | undefined = pageData?.contents;
        setContents(contentsData);
      } catch (error) {
        console.error("Error al cargar la página:", error);
      }
    }
    loadPage();
  }, [code])

  // Función para renderizar contenido basado en el tipo
  const renderContent = (content: IContent) => {
    switch (content?.contentType?.code) {
      case "hasImage":
        return <ImageComponent data={content} />;
      case "hasVideo":
        return <VideoComponent data={content} />;
      case "onlyDescription":
        return <OnlyDescriptionComponent data={content} />;
      case "hasDescription":
        return <HasDescriptionComponent data={content} />;
      case "onlyTitle":
        return <TitleComponent data={content} />;
      default:
        return null;
    }
  };

  return (
    <div>
      {contents && contents?.map((content: IContent) => {
        return (
          <div style={themes[content.theme]} key={content.id}>
            <Row justify={"center"} align={"middle"}>
              <Col span={20}>
                <Row justify={"center"}>
                  {renderContent(content)}
                </Row>
              </Col>
            </Row>
          </div>
        )
      })}
    </div >
  )
}

// Definición de componentes de contenido
function ImageComponent({ data }: { data: IContent }) {
  return (
    <img src={data.imageUrl} alt={data.imageUrl} />
  )
}
function VideoComponent({ data }: { data: IContent }) {
  return <video src={data.videoUrl} controls />;
}

function OnlyDescriptionComponent({ data }: { data: IContent }) {
  return <p>{data.description}</p>;
}

function HasDescriptionComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <OnlyDescriptionComponent data={data} />
    </Col>
  );
}

function TitleComponent({ data }: { data: IContent }) {
  return <h1>{data.title}</h1>;
}

// Themes 
const themes: React.CSSProperties[] = [
  {
    backgroundColor: "#c8d3a3",
    color: "black",
  },
  {
    backgroundColor: "#3b5a9d",
    color: "white"
  }
]

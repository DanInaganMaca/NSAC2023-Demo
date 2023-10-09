import React, { ReactNode, useEffect, useState } from "react"
import { IPage, IContent } from "../models/pages.model";
import { getOne } from "../api/pages.api";
import { Button, Card, Col, Row } from "antd";
import YouTube, { YouTubeProps } from "react-youtube";
import { Link } from "react-router-dom";

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
    sortedData;
  }, [code])

  console.log(contents);
  const sortedData = sortByID(contents);

  function sortByID(data: IContent[] | undefined): IContent[] | undefined {
    return data?.sort((a: IContent, b: IContent) => Number(a?.id) - Number(b?.id));
  }

  // Función para renderizar contenido basado en el tipo
  const renderContent = (content: IContent) => {
    switch (content?.contentType?.code) {
      case "onlyTitle":
        return <TitleComponent data={content} />;
      case "subTitle":
        return <SubTitleComponent data={content} />;
      case "titleAndSubTitle":
        return <TitleAndSubTitleComponent data={content} />;
      case "onlyDescription":
        return <DescriptionComponent data={content} />;
      case "onlyImage":
        return <ImageComponent data={content} />;
      case "onlyVideo":
        return <VideoComponent data={content} only={true} />;
      case "hasDescription":
        return <HasDescriptionComponent data={content} />;
      case "hasImageLeft":
        return <HasImageLeftComponent data={content} />;
      case "hasImageRight":
        return <HasImageRightComponent data={content} />;
      case "hasVideoLeft":
        return <HasVideoLeftComponent data={content} />;
      case "hasVideoRight":
        return <HasVideoRightComponent data={content} />;
      case "hasImageLeftWithoutTitle":
        return <HasImageLeftWithoutTitleComponent data={content} />;
      case "hasImageRightWithoutTitle":
        return <HasImageRightWithoutTitleComponent data={content} />;
      case "hasVideoLeftWithoutTitle":
        return <HasVideoLeftWithoutTitleComponent data={content} />;
      case "hasVideoRightWithoutTitle":
        return <HasVideoRightWithoutTitleComponent data={content} />;
      case "buttonInside":
        return <ButtonInsideComponent data={content} />;
      case "buttonOutside":
        return <ButtonOutsideComponent data={content} />;
      case "listOrder":
        return <ListOrderComponent data={content} />;
      case "listUnorder":
        return <ListUnorderComponent data={content} />;
      case "listConcatenada":
        return <ListConcatenadaComponent data={content} />;
      default:
        return null;
    }
  };

  return (
    <div>
      {sortedData && sortedData?.map((content: IContent) => {
        return (
          <div style={themes[content.theme]} key={content.id}>
            <Row justify={"center"} align={"middle"}>
              <Col span={18}>
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

// Tiene Imagen en la Izquierda
function HasImageLeftComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <ImageComponent data={data} />
        </Col>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
      </Row>
    </Col>
  )
}

// Tiene Imagen en la derecha
function HasImageRightComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
        <Col span={12}>
          <ImageComponent data={data} />
        </Col>
      </Row>
    </Col>
  )
}

function HasVideoLeftComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <VideoComponent data={data} />
        </Col>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
      </Row>
    </Col>
  );
}

function HasVideoRightComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
        <Col span={12}>
          <VideoComponent data={data} />
        </Col>
      </Row>
    </Col>
  );
}

function HasImageLeftWithoutTitleComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <ImageComponent data={data} />
        </Col>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
      </Row>
    </Col>
  )
}

// Tiene Imagen en la derecha
function HasImageRightWithoutTitleComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
        <Col span={12}>
          <ImageComponent data={data} />
        </Col>
      </Row>
    </Col>
  )
}

function HasVideoLeftWithoutTitleComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <VideoComponent data={data} />
        </Col>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
      </Row>
    </Col>
  );
}

function HasVideoRightWithoutTitleComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row align={"middle"} gutter={24}>
        <Col span={12}>
          <CardComponent>
            <DescriptionComponent data={data} card={true} />
          </CardComponent>
        </Col>
        <Col span={12}>
          <VideoComponent data={data} />
        </Col>
      </Row>
    </Col>
  );
}

function HasDescriptionComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row justify={"center"}>
        <DescriptionComponent data={data} />
      </Row>
    </Col>
  );
}

// Components
function TitleComponent({ data }: { data: IContent }) {
  return <h2>{data.title}</h2>;
}

function SubTitleComponent({ data }: { data: IContent }) {
  return <h3>{data.title}</h3>;
}

function TitleAndSubTitleComponent({ data }: { data: IContent }) {
  return (
    <Col span={24}>
      <Row justify={"center"}>
        <TitleComponent data={data} />
      </Row>
      <Row justify={"center"}>
        <h3>{data.imageUrl}</h3>
      </Row>
      <Row justify={"center"}>
        <DescriptionComponent data={data} />
      </Row>
    </Col>
  );
}

function DescriptionComponent({ data, card = false }: { data: IContent, card?: boolean }) {

  const parragraphStyle: React.CSSProperties = {
    fontSize: "0.85rem"
  }

  return <p style={card ? parragraphStyle : {}}>{data.description}</p>;
}

function ImageComponent({ data }: { data: IContent }) {
  // Styles
  const imageStyle: React.CSSProperties = {
    width: "100%",
    borderRadius: "8px 8px 8px 8px",
    boxShadow: "0px 8px 12px rgba(0, 0, 0, 0.2)"
  }

  return <img src={data.imageUrl} alt={data.title} style={imageStyle} />
}

function VideoComponent({ data, only = false }: { data: IContent, only?: boolean }) {
  const videoUrl = data?.videoUrl;

  if (!videoUrl) {
    return <div>No hay URL de video disponible.</div>
  }

  const videoId: string | undefined = extractVideoId(videoUrl);

  const opts: YouTubeProps["opts"] = {
    height: "390",
    width: "100%",
  }

  const onlyOpts: YouTubeProps["opts"] = {
    height: "390",
    width: "640"
  }

  const onlyVideoStyle: React.CSSProperties = {
    padding: "25px 0px"
  }

  return <YouTube videoId={videoId} opts={only ? onlyOpts : opts} style={onlyVideoStyle} />
}

function CardComponent({ children }: CardComponentProps) {
  // Styles
  const cardStyle: React.CSSProperties = {
    boxShadow: "0px 8px 12px rgba(0, 0, 0, 0.2)"
  }

  return (
    <Card style={cardStyle}>
      {children}
    </Card>
  )
}

function ButtonInsideComponent({ data }: { data: IContent }) {
  const path: string | undefined = data?.description;

  return (
    <Col span={8} style={{ margin: "10px 0px" }}>
      <Link to={path ? path : ""}>
        <Row justify={"center"}>
          <Button type={"default"} size={"large"} icon={data.imageUrl} ghost block>
            {data.title}
          </Button>
        </Row>
      </Link>
    </Col >
  )
}

function ButtonOutsideComponent({ data }: { data: IContent }) {
  const path: string | undefined = data?.description;

  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    e.preventDefault();
    window.open(path, "_blank");
  }

  return (
    <Col span={8} style={{ margin: "10px 0px" }}>
      <Row justify={"center"}>
        <Button type={"default"} size={"large"} icon={data.imageUrl} ghost block onClick={handleClick}>
          {data.title}
        </Button>
      </Row>
    </Col >
  )
}

function ListOrderComponent({ data }: { data: IContent }) {
  const list = data.description;

  const items = list?.split("-");

  return (
    <Col span={8}>
      <ol>
        {items && items.map((item, index) => (
          <li key={index}>{item.trim()}</li>
        ))}
      </ol>
    </Col>
  )
}

function ListUnorderComponent({ data }: { data: IContent }) {
  const list = data.description;

  const items = list?.split("-");

  return (
    <Col span={8}>
      <ul>
        {items && items.map((item, index) => (
          <li key={index}>{item.trim()}</li>
        ))}
      </ul>
    </Col>
  )
}

function ListConcatenadaComponent({ data }: { data: IContent }) {
  const list = data.description;

  const sections = list?.split("-");

  return (
    <Col span={8}>
      {sections && sections.map((section, index) => {
        const lines = section.split("\n");
        const header = lines[0].trim();
        const items = lines[1]?.split("*");
        // const items = lines.slice(1).map(item => item.trim());

        return (
          <div key={index}>
            <h5>{header}</h5>
            <ul>
              {items.map((item, itemIndex) => (
                <li key={itemIndex}>{item}</li>
              ))}
            </ul>
          </div>
        );
      })}
    </Col>
  )
}

// Themes 
const themes: React.CSSProperties[] = [
  {
    backgroundColor: "#001529",
    color: "white",
  },
  {
    backgroundColor: "#3b5a9d",
    color: "white",
  }
]

// Others
function extractVideoId(videoUrl: string) {
  // Patrones de URL de YouTube comunes
  const patterns = [
    /(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)/,
    /(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)/,
  ];

  for (const pattern of patterns) {
    const match = videoUrl.match(pattern);
    if (match && match[1]) {
      // Si hay un match en alguno de los patrones, devuelve el ID del video
      return match[1];
    }
  }

  // Si no se encontró un ID válido, puedes manejar el error o devolver null
  return undefined;
}

interface CardComponentProps {
  children: ReactNode
}

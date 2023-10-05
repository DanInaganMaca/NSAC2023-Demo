import { Carousel, Col } from "antd";
import slide1 from "../assets/slide1.png";
import slide2 from "../assets/slide2.png";
import slide3 from "../assets/slide3.png";
import slide4 from "../assets/slide4.png";
import slide5 from "../assets/slide5.png";

interface ImagenCarousel {
  id: string;
  src: string;
  alt: string;
}

const imagesCarousel: ImagenCarousel[] = [
  {
    id: "1",
    src: slide1,
    alt: "slide1"
  },
  {
    id: "2",
    src: slide2,
    alt: "slide2"
  },
  {
    id: "3",
    src: slide3,
    alt: "slide3"
  },
  {
    id: "4",
    src: slide4,
    alt: "slide4"
  },
  {
    id: "5",
    src: slide5,
    alt: "slide5"
  },
]

const textStyle: React.CSSProperties = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  textAlign: 'center',
  color: 'white', // Cambia el color del texto según tu diseño
};

const imgStyle: React.CSSProperties = {
  width: "100%",
  height: "100%",
  objectFit: "cover",
};

export function ImageCarousel() {

  return (
    <Carousel autoplay style={{ width: "100%", height: "fit-content", justifyContent: "center" }}>
      {imagesCarousel.map((imagen: ImagenCarousel) => {
        return (
          <Col key={imagen.id} span={24}>
            <img src={imagen.src} alt={imagen.alt} style={imgStyle} />
            <h1 style={textStyle}>Biodiversidad</h1>
          </Col>
        )
      })}
    </Carousel>
  )
}

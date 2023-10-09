import { Carousel, Col } from "antd";
// import slide1 from "../assets/slide1.png";
import slide2 from "../assets/slide2.png";
import slide3 from "../assets/slide3.png";
import slide4 from "../assets/slide4.png";
import slide5 from "../assets/slide5.png";

interface ImagenCarousel {
  id: string;
  src: string;
  alt: string;
  description?: string;
}

const imagesCarousel: ImagenCarousel[] = [
  {
    id: "2",
    src: slide2,
    alt: "slide2",
    description: "(GCFR), is known for its exceptional biodiversity and unique geology due to the fold belt."
  },
  {
    id: "3",
    src: slide3,
    alt: "slide3",
    description: "The Greater Cape Floristic Region of South Africa has the richest temperate flora and the third highest marine endemism in the world."
  },
  {
    id: "4",
    src: slide4,
    alt: "slide4",
    description: "Fynbos is a type of vegetation native to South Africa and is known for its botanical diversity."
  },
  {
    id: "5",
    src: slide5,
    alt: "slide5",
    description: "The South African coast is rich in marine life, and the area known as the 'Bay of Whales'."
  },
]

const textStyle: React.CSSProperties = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  textAlign: 'center',
  color: 'white', // Cambia el color del texto según tu diseño
  textShadow: "0px 8px 12px rgba(0, 0, 0, 0.8)"
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
            <h3 style={textStyle}>{imagen.description}</h3>
          </Col>
        )
      })}
    </Carousel>
  )
}

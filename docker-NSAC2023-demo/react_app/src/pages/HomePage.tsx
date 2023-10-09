import { ContentPage } from "../components/ContentPage";
import { ImageCarousel } from "../components/ImageCarousel";


export default function HomePage() {

  return (
    <>
      <ImageCarousel />
      <ContentPage key={'home'} code={'home'} />
    </>
  )
}

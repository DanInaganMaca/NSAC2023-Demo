import { ContentPage } from "../components/ContentPage";
import { ImageCarousel } from "../components/ImageCarousel";


export function HomePage() {

  return (
    <>
      <ImageCarousel />
      <ContentPage key={'home'} code={'home'} />
    </>
  )
}

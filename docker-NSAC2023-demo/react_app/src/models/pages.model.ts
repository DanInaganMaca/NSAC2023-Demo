export interface IPage {
  id: string;
  title: string;
  code: string;
  nameTab: string;
  createAt: string;
  contents: IContent[];
}

export interface IContentType {
  id: string;
  name: string;
  code: string;
  createAt: string;
}

export interface IContent {
  id: string;
  contentType: IContentType;
  theme: number;
  title?: string;
  description?: string;
  imageUrl?: string;
  videoUrl?: string;
}

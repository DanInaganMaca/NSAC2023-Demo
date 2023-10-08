export function ImageHeader({ img }: { img: string }) {

  return (
    <div style={{ background: "#001529" }}>
      <img src={img} width={"100%"} />
    </div>
  )
}

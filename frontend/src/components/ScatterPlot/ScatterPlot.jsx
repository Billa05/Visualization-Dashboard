import { ResponsiveScatterPlot } from "@nivo/scatterplot";
import { useContext } from "react";
import { ChartsDataContext } from "../../ChartsContextProvider";
import { useEffect, useState } from "react";
import axios from "axios";
// make sure parent container have a defined height when using
// responsive component, otherwise height will be 0 and
// no chart will be rendered.
// website examples showcase many properties,
// you'll often use just a few of them.
const MyResponsiveScatterPlot = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:5000/")
      .then((res) => {
        // console.log(res.data);
        setData(res.data);
      })
      .catch((error) => console.error(error));
  }, []);

  //   const { data } = useContext(ChartsDataContext);
  return (
    <>
      {data && (
        <ResponsiveScatterPlot
          data={data.scatterchart}
          margin={{ top: 60, right: 140, bottom: 70, left: 90 }}
          xScale={{ type: "linear", min: 0, max: "auto" }}
          xFormat=" >-.2f"
          yScale={{ type: "linear", min: 0, max: "auto" }}
          yFormat=" >-.2f"
          blendMode="multiply"
          axisTop={null}
          axisRight={null}
          axisBottom={{
            orient: "bottom",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "weight",
            legendPosition: "middle",
            legendOffset: 46,
            truncateTickAt: 0,
          }}
          axisLeft={{
            orient: "left",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "size",
            legendPosition: "middle",
            legendOffset: -60,
            truncateTickAt: 0,
          }}
          legends={[
            {
              anchor: "bottom-right",
              direction: "column",
              justify: false,
              translateX: 130,
              translateY: 0,
              itemWidth: 100,
              itemHeight: 12,
              itemsSpacing: 5,
              itemDirection: "left-to-right",
              symbolSize: 12,
              symbolShape: "circle",
              effects: [
                {
                  on: "hover",
                  style: {
                    itemOpacity: 1,
                  },
                },
              ],
            },
          ]}
        />
      )}
    </>
  );
};

export default MyResponsiveScatterPlot;

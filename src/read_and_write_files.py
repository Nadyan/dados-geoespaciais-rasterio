import rasterio
from rasterio.plot import show


def show_data(gds, title=""):
    print(f"Metadados: {gds.meta}")
    print(f"Dados: {gds.read()}")

    show(gds, title=title)


def write_data(gds):
    data = gds.read()
    with rasterio.open(fp="../output_data/nepal_lc_2020_new.tif",
        mode="w",
        driver=gds.driver,
        height=gds.height,
        width=gds.width,
        count=gds.count,
        crs=gds.crs,
        transform=gds.transform,
        dtype=data.dtype,
        nodata=gds.nodata
    ) as file:
        file.write(data)


def main():
    gds = rasterio.open("../data/nepal_lc_2020.tif")

    show_data(gds, "Original dataset")
    write_data(gds)

    new_gds = rasterio.open("../output_data/nepal_lc_2020_new.tif")

    show_data(new_gds, "Edited dataset")


if __name__ == "__main__":
    main()

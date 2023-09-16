# Welcome to Backend UMKM

API ini berisi list produk dan search produk

## Installation

Run the following command to clone the repository, and install the dependencies.

```sh
git clone https://github.com/annalitcz/backend-umkm
cd backend-umkm
pip install -r requirement.txt
```

start the server

```sh
python app.py
```

## Response

- get all product:

  ```link
  /api/products
  ```

  Data:

  ```json
  {
    "message": "API produk berhasil diakses.",
    "products": [
      {
        "deskripsi": "Deskripsi Produk 1",
        "gambar": "/assets/image_2023-08-06_23-20-36.png",
        "harga": 100.0,
        "nama": "Produk 1"
      },
      {
        "deskripsi": "Deskripsi Produk 2",
        "gambar": "/assets/image_2023-08-06_23-20-36.png",
        "harga": 150.0,
        "nama": "Produk 2"
      },
      {
        "deskripsi": "Deskripsi Produk 3",
        "gambar": "/assets/image_2023-08-06_23-20-36.png",
        "harga": 50.0,
        "nama": "Produk 3"
      }
    ],
    "status": "Success"
  }
  ```

- Search Products

  ```link
  /api/products/search?query=produk%201
  ```

  Data:

  ```json
  {
    "message": "Hasil pencarian produk",
    "products": [
      {
        "deskripsi": "Deskripsi Produk 2",
        "gambar": "/assets/image_2023-08-06_23-20-36.png",
        "harga": 150.0,
        "nama": "Produk 2"
      }
    ],
    "status": "Success"
  }
  ```

## Support me

<a href="https://saweria.co/AnzzID" style="background-color: #0074D9; color: #FFFFFF; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Saweria</a>


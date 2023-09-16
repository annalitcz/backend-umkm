# Welcome to Backend UMKM

![iconku](src/icon.jpeg)

API ini berisi list produk dan search produk, kalo ingin tambah fitur ya koding sendiri.

## Installation

Run the following command to clone the repository, and install the dependencies.

- clone repository

```sh
git clone https://github.com/annalitcz/backend-umkm
```

- open the folder
  
```sh
cd backend-umkm
```

- install library
  
```sh
pip install -r requirements.txt
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

  __OR__

  ```link
  /api/products/search?query={query}
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

[Saweria](https://saweria.co/AnzzID)

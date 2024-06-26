import React, { useContext } from "react";
import { ProductContext } from "../contexts/ProductContext";
import Product from "../components/Product";
import Hero from "../components/Hero";
import { BarLoader } from "react-spinners";

const Home = () => {
  // get product from context
  const { products, loading } = useContext(ProductContext);

  // get men and women clothing
  const filteredProduct = products.filter((item) => {
    return (
      item.category === "men's clothing" || item.category === "women's clothing"
    );
  });

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <BarLoader size={50} color={"#123abc"} loading={loading} />
      </div>
    );
  }

  return (
    <div>
      <Hero />
      <section className="py-16">
        <div className="container mx-auto">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 gap-[30px] max-w-sm mx-auto md:max-w-none md:mx-0">
            {filteredProduct.map((product) => {
              return <Product product={product} key={product.id} />;
            })}
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;

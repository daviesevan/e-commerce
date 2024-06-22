import React, { createContext, useState, useEffect } from "react";
// create context 
export const ProductContext = createContext()

const ProductProvider = ({children}) => {
    // product state 
    const [products, setProducts] = useState([])
    const [loading, setLoading] = useState(false)
    useEffect(()=>{
        const fetchProducts = async () =>{
            setLoading(true)
            const res = await fetch('https://fakestoreapi.com/products')
            const data = await res.json()
            // console.table(data)
            setProducts(data)
            setLoading(false)
            }
            fetchProducts()
    },[])
  return <ProductContext.Provider value={{products}} >
    {children}
  </ProductContext.Provider>;
};

export default ProductProvider;

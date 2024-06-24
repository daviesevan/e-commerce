import React, { createContext, useState, useEffect } from "react";
import fetchInventory from '../Api';

// Create context 
export const ProductContext = createContext();

const ProductProvider = ({ children }) => {
    // Product state 
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchProducts = async () => {
            setLoading(true);
            try {
                const res = await fetchInventory.get('/inventory/all');
                setProducts(res.data);
            } catch (error) {
                console.error('Error fetching inventory:', error);
            }
            setLoading(false);
        };
        fetchProducts();
    }, []);

    return (
        <ProductContext.Provider value={{ products, loading }}>
            {children}
        </ProductContext.Provider>
    );
};

export default ProductProvider;

import { useState, useEffect } from 'react'
// No need to import App.css anymore!

function App() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [searchQuery, setSearchQuery] = useState("")

  useEffect(() => {
    fetch('http://127.0.0.1:8000/ai-insights')
      .then(response => response.json())
      .then(apiData => {
        setData(apiData)
        setLoading(false)
      })
  }, [])

  const getFilteredProducts = () => {
    if (!data) return[]
    const allProducts = Object.keys(data.sales_summary)
    return allProducts.filter(product => 
      product.toLowerCase().includes(searchQuery.toLowerCase())
    )
  }

  return (
    // Tailwind: bg-gray-50 (light gray background), min-h-screen (full height), p-8 (padding)
    <div className="bg-gray-50 min-h-screen p-8 font-sans text-gray-800">
      
      {/* Tailwind: text-center, text-3xl (large text), font-bold, mb-8 (margin bottom) */}
      <h1 className="text-center text-3xl font-bold mb-8">🚀 AI Sales Dashboard</h1>
      
      {loading ? (
        <p className="text-center text-lg text-gray-500">Loading AI Insights...</p>
      ) : (
        // Tailwind: max-w-4xl (max width), mx-auto (center horizontally)
        <div className="max-w-4xl mx-auto">
          
          {/* Tailwind: flex, gap-6 (space between items) */}
          <div className="flex flex-col md:flex-row gap-6 mb-8">
            
            {/* Card 1 - Tailwind: bg-white, shadow-md, rounded-xl, p-6, flex-1 */}
            <div className="bg-white shadow-md rounded-xl p-6 flex-1 text-center">
              <h2 className="text-xl font-semibold mb-2">🏆 Best Seller</h2>
              <p className="text-4xl font-bold text-slate-800 my-4">{data.best_seller}</p>
              <p className="text-gray-600">Total Revenue: ${data.sales_summary[data.best_seller]}</p>
            </div>

            {/* Card 2 - AI Card - Tailwind: bg-gradient, text-white, shadow-md, rounded-xl, p-6, flex-1 */}
            <div className="bg-linear-to-br from-purple-500 to-indigo-500 text-white shadow-md rounded-xl p-6 flex-1 text-center">
              <h2 className="text-xl font-semibold mb-4">🤖 AI Recommendation</h2>
              <p className="text-sm leading-relaxed">{data.ai_recommendation}</p>
            </div>
          </div>

          {/* Search Input - Tailwind: w-full, p-3, border, rounded-lg, focus:ring */}
          <input 
            type="text" 
            className="w-full p-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-400 mb-6"
            placeholder="🔍 Search for a product..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />

          {/* List Card */}
          <div className="bg-white shadow-md rounded-xl p-6">
            <h2 className="text-xl font-semibold mb-4 border-b pb-2">Product Revenues</h2>
            <ul>
              {getFilteredProducts().map(product => (
                // Tailwind: flex, justify-between, p-3, border-b
                <li key={product} className="flex justify-between p-3 border-b border-gray-100 hover:bg-gray-50 transition-colors">
                  <strong className="text-gray-700">{product}</strong>
                  <span className="text-indigo-600 font-medium">${data.sales_summary[product]}</span>
                </li>
              ))}
              {getFilteredProducts().length === 0 && (
                <p className="text-gray-500 italic mt-4">No products found.</p>
              )}
            </ul>
          </div>

        </div>
      )}
    </div>
  )
}

export default App
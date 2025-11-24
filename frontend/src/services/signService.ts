const signService = {
    searchSigns: async (searchTerm: string) => {
        const response = await fetch(`/api/signs?q=${encodeURIComponent(searchTerm)}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    }
} 

export default signService;
from django.shortcuts import render, redirect
import folium
import pandas as pd
import webbrowser
from geopy.geocoders import Nominatim


def report_home(request):
    if request.method == "POST":
        location = request.POST.get("location")
        radius = request.POST.get("radius")
        loc = Nominatim(user_agent="GetLoc")

        # Get the geodataframe for the location
        getLoc = loc.geocode(location)

        # Print the address, latitude, and longitude

        start_point = [getLoc.latitude, getLoc.longitude]

        # Create a DataFrame with zipcodes and coordinates
        data = pd.DataFrame({
            'Zipcode': ['ZIP1', 'ZIP2', 'ZIP3', "ZIP4", "ZIP5"],
            'Latitude': [21.144248, 21.135394, 21.151578, 21.110383, 21.120441],
            'Longitude': [79.108952, 79.079147, 79.096908, 79.112890, 79.030198]
        })

        # Initialize the map
        m = folium.Map(location=start_point, zoom_start=15)
        folium.Marker(
            location=start_point,
            popup=f"disaster zone",
            icon=folium.Icon(color='red')
        ).add_to(m)

        # Replace with your desired radius (in meters)
        radius_meters = int(radius)

        # Add the circle to the map
        folium.Circle(
            location=start_point,
            radius=radius_meters,
            color='blue',  # Circle outline color
            fill=True,  # Fill the circle
            fill_color='red',  # Circle fill color
            fill_opacity=0.3,  # Opacity of the fill
            popup=f"disaster zone",  # Popup text (optional)
        ).add_to(m)

        # Add markers for each location
        for index, row in data.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup="Rescue Agency"
            ).add_to(m)

        for index, row in data.iterrows():
            folium.PolyLine(
                locations=[start_point, [row['Latitude'], row['Longitude']]],
                color='blue',
                weight=3,
                opacity=1,
                popup="Route"
            ).add_to(m)

        m.save("./templates/map.html")

        return redirect("report:map_display")

    return render(request, "report/report.html")


def map_display(request):
    return render(request, "map.html")

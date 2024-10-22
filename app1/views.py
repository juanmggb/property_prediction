import csv
from collections import Counter
import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Prediction
import numpy as np

# Create your views here.


def prediction_list(request):
    predictions = Prediction.objects.all().order_by("-id")

    prediction_data = [
        {
            "id": prediction.id,
            "x": prediction.x,
            "y": prediction.y,
            "z_exp": prediction.z_exp,
            "z_pred": prediction.z_pred,
        }
        for prediction in predictions
    ]

    return render(
        request, "app1/prediction_list.html", {"predictions": prediction_data}
    )


def upload_csv(request):
    if request.method == "POST":
        file = request.FILES["csv_file"]
        decoded_file = file.read().decode("utf-8").splitlines()
        reader = csv.reader(decoded_file)

        next(reader)

        for row in reader:
            x, y, z = map(float, row)

            z_pred = z + 0.5 * random.uniform(0, 1)

            # Save to database
            Prediction.objects.create(x=x, y=y, z_exp=z, z_pred=z_pred)

        return redirect("prediction_list")

    return render(request, "app1/upload.html")


def plot_data(request):

    return render(request, "app1/plot.html")


def get_chart_data(request, plot_type):
    predictions = Prediction.objects.all()

    print("plot_type", plot_type)

    if plot_type == "predVsExp":
        z_exp = [pred.z_exp for pred in predictions]
        z_pred = [pred.z_pred for pred in predictions]

        return JsonResponse(
            {
                "z_exp": z_exp,
                "z_pred": z_pred,
            }
        )
    elif plot_type == "ceteneDis":
        cetene_values = [
            pred.z_exp for pred in predictions
        ]  # Use the correct attribute

        # Define the bins for frequency ranges (0 to 100)
        bins = np.arange(0, 101, 10)  # 0-10, 10-20, ..., 90-100
        frequencies, edges = np.histogram(cetene_values, bins=bins)

        return JsonResponse(
            {
                "cetene_bins": [
                    (int(edges[i]), int(edges[i + 1])) for i in range(len(edges) - 1)
                ],  # Convert to int
                "frequencies": frequencies.tolist(),  # Convert frequencies to a list
            }
        )

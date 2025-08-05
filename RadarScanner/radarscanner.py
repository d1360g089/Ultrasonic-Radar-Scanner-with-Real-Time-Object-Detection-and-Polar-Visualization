

import serial
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import cm 
from math import isclose
import time



serial_data = serial.Serial('com3', 9600)

angles = []
distances = []


fig = plt.figure()
ax = plt.subplot(projection='polar')
scatter, = ax.plot([], [], 'mo', markersize=3)
sweep_line, = ax.plot([], [], 'r-', lw=3)
closest_dot, = ax.plot([],[], 'go', markersize=8)


ax.set_rmax(30)

fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.tick_params(colors='lime')
for spine in ax.spines.values():
    spine.set_color('lime')

rings = [5,10,15,20,25,30]
ax.set_rticks(rings)
ax.set_rlabel_position(180)

info_text = ax.text(
    -.25, 1.025, "", transform=ax.transAxes,
    fontsize=16,
    color = 'red',
    bbox=dict(boxstyle="round", facecolor='black', edgecolor='lime')

)


closeObj_text = ax.text(
     .8, 1.025, "", transform=ax.transAxes,
    fontsize=16,
    color = 'red',
    bbox=dict(boxstyle="round", facecolor='black', edgecolor='lime')

)


lock_on = False
lock_threshold = 10






def update(frame):


    global angles, distances, lock_on

    while serial_data.in_waiting:
        line = serial_data.readline().decode().strip()

        try:
            dist_str, angle_str = line.split(",")
            angle_deg = float(angle_str)
            angle_rad = np.radians(angle_deg)

            dist = float(dist_str)
            angles.append(angle_rad)
            distances.append(dist)
            scatter.set_data(angles, distances)
            ax.set_rmax(30)
            
            if angles:
                sweep_angle = angles[-1]
                sweep_line.set_data([sweep_angle, sweep_angle], [0, 40])

            if distances:
                min_index = np.argmin(distances)
                min_angle = angles[min_index]
                min_dist = distances[min_index]
                closest_dot.set_data([min_angle], [min_dist])

                info_text.set_text(f"Angle: {angle_deg:.0f}°\nDist: {dist:.1f} in")

            

        except ValueError:
            continue

    
    
    
    angle_threshold = np.radians(5)      # ~5 degrees
    distance_threshold = 10


    if len(angles) > 2:
        clusters = []
        current_cluster = []


        for i in range(len(angles)):
            a = angles[i]
            d = distances[i]

            if not current_cluster:
                current_cluster.append((a, d))
                continue

            prev_a, prev_d = current_cluster[-1]
            da = abs(a - prev_a)
            dd = abs(d - prev_d)

            if da < angle_threshold and dd < distance_threshold:
                current_cluster.append((a, d))
            else:
                if len(current_cluster) > 1:
                    clusters.append(current_cluster)
                current_cluster = [(a, d)]

        if len(current_cluster) > 1:
            clusters.append(current_cluster)


       
        # ----- Find Closest Cluster by Mean Distance & Mean Angle -----
        if clusters:
            closest_cluster = min(clusters, key=lambda c: np.mean([d for _, d in c]))
            centroid_angle = np.mean([a for a, _ in closest_cluster])
            centroid_dist = np.mean([d for _, d in closest_cluster])
            closest_dot.set_data([centroid_angle], [centroid_dist])

    
            closeObj_text.set_text(f"Closest Obj: \n{centroid_dist:.1f} in")
            
        
    return scatter, sweep_line, closest_dot
    


ani = FuncAnimation(fig, update, interval=50)
plt.show()




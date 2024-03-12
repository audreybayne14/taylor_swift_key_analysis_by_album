# import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# loading data

# create a DataFrame from the scraped spotify key signature data
    # the bracketed numbers after each key signature are the counts of songs in each album in order of release
keys_by_album = {
    'C' :[1, 2, 1, 5, 2, 7, 6, 3, 4, 6, 0], 'F' :[2, 6, 1, 1, 4, 1, 1, 2, 2, 1, 0], 'Bb' :[1, 1, 1, 0, 0, 0, 2, 1, 1, 3, 0], 'Eb' :[0, 1, 0, 1, 1, 0, 0, 2, 0, 0, 0],
    'Ab' :[2, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0], 'Db' :[0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0], 'Ebm' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Bbm' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Fm' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Cm' :[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 'Gm' :[0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0], 'Dm' :[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'Am' :[0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0], 'Em' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Bm' :[0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0], 'Gbm' :[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Dbm' :[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 'Abm' :[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 'Gb' :[0, 3, 0, 2, 0, 0, 0, 1, 0, 1, 0], 'B' :[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    'E' :[1, 1, 4, 8, 2, 0, 1, 1, 1, 2, 0], 'A' :[1, 1, 0, 0, 1, 1, 2, 1, 1, 3, 0], 'D' :[3, 6, 2, 3, 1, 1, 2, 3, 1, 1, 0], 'G' :[2, 3, 4, 8, 3, 0, 1, 1, 1, 3, 0]
              }

# index_labels are album titles
index_labels=['Debut', 'Fearless', 'Speak Now', 'Red', 'Birth', 'Reputation', 'Lover', 'Folklore', 'Evermore', 'Midnights', 'Blank']
df = pd.DataFrame(keys_by_album,index=index_labels)
print(df)


# building the radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['ALBUM'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='HEX', linewidth=1)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')

# debut radar chart

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Debut'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#A9C2A4', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# fearless radar chart

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Fearless'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#E5B875', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# speak now radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Speak Now'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#C4A5C5', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# red radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Red'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#7B3744', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# 1989 radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Birth'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#B0D9EB', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# reputation radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Reputation'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#7E7377', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# lover radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Lover'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#F0A9C7', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# folklore radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Folklore'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#C6C1BB', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# evermore radar chart

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Evermore'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#BDA58B', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


# midnights radar chart

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Midnights'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#3A4A89', linewidth=2.5)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), [])

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


blank radar chart (FOR AUDREY ONLY)

# we will need to repeat all of step three for each album's radar chart
    # the ONLY things you need to change are 'ALBUM' and the two instances of 'HEX'

# the attributes we will plot in the radar chart (keys)
labels = ['C','F','Bb','Eb','Ab','Db','Ebm','Bbm','Fm','Cm','Gm','Dm','Am','Em','Bm','Gbm','Dbm','Abm','Gb','B','E','A','D','G']

# now, we can plot an album
values = df.loc['Blank'].tolist()

# number of variables we're plotting (key signatures)
num_vars = len(labels)

# split the circle into even parts and save the angles
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# complete the loop
values += values[:0]
angles += angles[:0]

# chart sizing
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# draw the outline of the data
    # i am using hex codes of colors i chose for each album
ax.plot(angles, values, color='#3A4A89', linewidth=0)

# fix axis to go in the right order
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(+1)

# draw axis lines for each angle and label
ax.set_thetagrids(np.degrees(angles), labels)

# ensure radar goes from 0 to 7 for standardization across charts
ax.set_ylim(0, 7)

# remove tick labels
ax.set_yticklabels([])

# add some custom styling
    # change the color of the tick labels
ax.tick_params(colors='#222222')
    # make the y-axis labels smaller
ax.tick_params(axis='y', labelsize=8)
    # change the color of the circular gridlines
ax.grid(color='#ECEDEF')
    # change the color of the outermost gridline (the spine)
ax.spines['polar'].set_color('#222222')


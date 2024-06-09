"""add learning_proccess

Revision ID: ec6fe90cea5a
Revises: 9f1d8f2fea4e
Create Date: 2024-06-08 02:10:36.192104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec6fe90cea5a'
down_revision: Union[str, None] = '9f1d8f2fea4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'building',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('lng', sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'lecture_period',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('start_at', sa.TIME(), nullable=False),
        sa.Column('end_at', sa.TIME(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'subject',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('is_professional', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'classroom',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('max_student_capacity', sa.Integer(), nullable=False),
        sa.Column('features', sa.String(), nullable=True),
        sa.Column('building_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['building_id'], ['building.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'lecture',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_full_group', sa.Boolean(), nullable=False),
        sa.Column('subject_id', sa.Integer(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), nullable=True),
        sa.Column('classroom_id', sa.Integer(), nullable=True),
        sa.Column('lecture_period_id', sa.Integer(), nullable=False),
        sa.Column('group_id', sa.Integer(), nullable=False),
        sa.Column('lection_date', sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(['classroom_id'], ['classroom.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
        sa.ForeignKeyConstraint(['lecture_period_id'], ['lecture_period.id'], ),
        sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'grade_event',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('grade_type', sa.Enum('lecture_grade', 'semester_grade', 'module_grade', 'control_grade', 'independent_work_grade', 'default_grade', name='gradetype'), nullable=False),
        sa.Column('lection_id', sa.Integer(), nullable=True),
        sa.Column('subject_id', sa.Integer(), nullable=True),
        sa.Column('date_event', sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(['lection_id'], ['lecture.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'grade',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('desc', sa.String(), nullable=True),
        sa.Column('grade_event_id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('teacher_id', sa.Integer(), nullable=False),
        sa.Column('mark_type', sa.Enum('mark100', 'mark12', name='marktype'), nullable=False),
        sa.Column('mark', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['grade_event_id'], ['grade_event.id'], ),
        sa.ForeignKeyConstraint(['student_id'], ['student.id'], ondelete='SET NULL'),
        sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grade')
    op.drop_table('grade_event')
    op.drop_table('lecture')
    op.drop_table('classroom')
    op.drop_table('subject')
    op.drop_table('lecture_period')
    op.drop_table('building')
    # ### end Alembic commands ###